// Azure AI Search service module — resource-group scoped.
param location string
param searchServiceName string

@allowed([
  'free'
  'basic'
  'standard'
])
param sku string

@allowed([
  'disabled'
  'free'
  'standard'
])
param semanticSearchTier string

@description('Principal ID to grant Search Index Data Contributor + Search Service Contributor to (the GitHub Actions OIDC identity). Leave empty to skip.')
param indexerPrincipalId string = ''

resource search 'Microsoft.Search/searchServices@2025-05-01' = {
  name: searchServiceName
  location: location
  sku: {
    name: sku
  }
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    replicaCount: 1
    partitionCount: 1
    hostingMode: 'Default'
    publicNetworkAccess: 'enabled'
    semanticSearch: semanticSearchTier
    authOptions: {
      aadOrApiKey: {
        aadAuthFailureMode: 'http401WithBearerChallenge'
      }
    }
  }
  tags: {
    project: 'policy-navigator'
    phase: 'phase1-rag'
  }
}

// Search Index Data Contributor — lets the indexing workflow upsert documents.
var searchIndexDataContributorRoleId = '8ebe5a00-799e-43f5-93ac-243d3dce84a7'
// Search Service Contributor — lets the indexing workflow create/update the index definition itself.
var searchServiceContributorRoleId = '7ca78c08-252a-4471-8644-bb5ff32d4ba0'

resource indexDataContributorAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (!empty(indexerPrincipalId)) {
  name: guid(search.id, indexerPrincipalId, searchIndexDataContributorRoleId)
  scope: search
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', searchIndexDataContributorRoleId)
    principalId: indexerPrincipalId
    principalType: 'ServicePrincipal'
  }
}

resource serviceContributorAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (!empty(indexerPrincipalId)) {
  name: guid(search.id, indexerPrincipalId, searchServiceContributorRoleId)
  scope: search
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', searchServiceContributorRoleId)
    principalId: indexerPrincipalId
    principalType: 'ServicePrincipal'
  }
}

output searchServiceName string = search.name
output endpoint string = 'https://${search.name}.search.windows.net'

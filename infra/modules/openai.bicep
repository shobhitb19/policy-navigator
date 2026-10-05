// Dedicated Azure OpenAI (Cognitive Services, kind 'OpenAI') resource + embedding deployment.
param location string
param accountName string
param embeddingModelName string
param embeddingModelVersion string
param embeddingCapacity int

@description('Principal ID to grant Cognitive Services OpenAI User to (the GitHub Actions OIDC identity). Leave empty to skip.')
param indexerPrincipalId string = ''

resource openAi 'Microsoft.CognitiveServices/accounts@2025-06-01' = {
  name: accountName
  location: location
  kind: 'OpenAI'
  sku: {
    name: 'S0'
  }
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    customSubDomainName: accountName
    publicNetworkAccess: 'Enabled'
    disableLocalAuth: false
  }
  tags: {
    project: 'policy-navigator'
    phase: 'phase1-rag'
  }
}

resource embeddingDeployment 'Microsoft.CognitiveServices/accounts/deployments@2025-06-01' = {
  parent: openAi
  name: embeddingModelName
  sku: {
    name: 'Standard'
    capacity: embeddingCapacity
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: embeddingModelName
      version: empty(embeddingModelVersion) ? null : embeddingModelVersion
    }
    versionUpgradeOption: 'OnceCurrentVersionExpired'
  }
}

// Cognitive Services OpenAI User — lets the indexing workflow call the embeddings endpoint
// via DefaultAzureCredential without an API key.
var cognitiveServicesOpenAiUserRoleId = '5e0bd9bd-7b93-4f28-af87-19fc36ad61bd'

resource openAiUserAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (!empty(indexerPrincipalId)) {
  name: guid(openAi.id, indexerPrincipalId, cognitiveServicesOpenAiUserRoleId)
  scope: openAi
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', cognitiveServicesOpenAiUserRoleId)
    principalId: indexerPrincipalId
    principalType: 'ServicePrincipal'
  }
}

output accountName string = openAi.name
output endpoint string = openAi.properties.endpoint
output embeddingDeploymentName string = embeddingDeployment.name

// Phase 1 infrastructure for the policy-navigator Azure AI Search RAG layer.
//
// Deploys (subscription scope):
//   - a new resource group
//   - an Azure AI Search service (Basic tier, semantic ranker enabled)
//   - a dedicated Azure OpenAI (Cognitive Services, kind 'OpenAI') resource with a single
//     text-embedding deployment
//
// See /docs/AZURE_RAG_SETUP.md for the full design rationale and how to deploy this.
targetScope = 'subscription'

@description('Azure region for all resources.')
param location string = 'australiaeast'

@description('Resource group name.')
param resourceGroupName string = 'rg-policy-navigator'

@description('Resource naming prefix.')
param namePrefix string = 'policynav'

@description('Azure AI Search SKU. Basic supports the semantic ranker and comfortably handles this repo\'s size (254 claims); move to standard only if replica/partition/storage limits are hit.')
@allowed([
  'free'
  'basic'
  'standard'
])
param searchSku string = 'basic'

@description('Semantic search (semantic ranker) tier for Azure AI Search.')
@allowed([
  'disabled'
  'free'
  'standard'
])
param semanticSearchTier string = 'standard'

@description('Embedding model to deploy on the Azure OpenAI resource.')
param embeddingModelName string = 'text-embedding-3-large'

@description('Embedding model version. Leave empty to use the provider default version.')
param embeddingModelVersion string = ''

@description('Deployed capacity (in thousands of tokens per minute) for the embedding deployment.')
param embeddingCapacity int = 30

@description('Principal ID of the Entra ID app/managed identity used by the GitHub Actions OIDC indexing workflow. Leave empty to skip role assignment at deploy time and grant it later (see docs).')
param indexerPrincipalId string = ''

resource rg 'Microsoft.Resources/resourceGroups@2024-11-01' = {
  name: resourceGroupName
  location: location
  tags: {
    project: 'policy-navigator'
    phase: 'phase1-rag'
  }
}

module search 'modules/search.bicep' = {
  name: 'search-deployment'
  scope: rg
  params: {
    location: location
    searchServiceName: '${namePrefix}-search'
    sku: searchSku
    semanticSearchTier: semanticSearchTier
    indexerPrincipalId: indexerPrincipalId
  }
}

module openai 'modules/openai.bicep' = {
  name: 'openai-deployment'
  scope: rg
  params: {
    location: location
    accountName: '${namePrefix}-openai'
    embeddingModelName: embeddingModelName
    embeddingModelVersion: embeddingModelVersion
    embeddingCapacity: embeddingCapacity
    indexerPrincipalId: indexerPrincipalId
  }
}

output resourceGroupName string = rg.name
output searchServiceName string = search.outputs.searchServiceName
output searchServiceEndpoint string = search.outputs.endpoint
output openAiAccountName string = openai.outputs.accountName
output openAiEndpoint string = openai.outputs.endpoint
output embeddingDeploymentName string = openai.outputs.embeddingDeploymentName

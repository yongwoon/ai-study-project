# Exampel Selectgor

## MaxMarginalRelevanceExampleSelector and SemanticSimilarityExampleSelector는

LangChain의 MaxMarginalRelevanceExampleSelector와 SemanticSimilarityExampleSelector는 모두 예제 선택기(Example Selector)로,
모델 학습이나 추론 시 사용할 예제를 선택하는 데 사용됩니다.
그러나 이 두 선택기는 예제를 선택하는 방법에서 차이가 있습니다. 아래는 두 선택기의 주요 차이점을 설명합니다:

- MaxMarginalRelevanceExampleSelector
  - 목적: 다양성과 관련성을 동시에 고려하여 예제를 선택합니다.
  - 알고리즘: Maximal Marginal Relevance (MMR) 알고리즘을 사용합니다. 이 알고리즘은 예제의 관련성과 다양성을 균형 있게 평가합니다.
  - 사용 사례: 다양한 예제를 포함하여 모델이 다양한 시나리오에 대해 학습할 수 있도록 할 때 유용합니다.
  - 특징: 예제 간의 유사도와 쿼리와의 유사도를 모두 고려하여 예제를 선택합니다. 이를 통해 중복되는 예제를 피하고 다양한 예제를 선택할 수 있습니다.
  - MMM algorithm 의 작동방식
    - 첫번쨰 단계에세느느 가장 관련성 높은 항목을 선택합니다.
    - 이후의 각 단계에서는 현재 선택된 항목들과 곤련성은 높으면서도 가정 차별화된 항목을 찾아 선택합니다. 이는 λ 값에 의해 조절되며, 이 값이 클수록 관련성을, 작을수록 다양성을 더 중시합니다.
- SemanticSimilarityExampleSelector
  - 목적: 주로 예제와 쿼리 간의 의미적 유사성을 기준으로 예제를 선택합니다.
  - 알고리즘: 의미적 유사성을 계산하는 알고리즘을 사용합니다. 예를 들어, 코사인 유사도나 유클리드 거리 등을 사용할 수 있습니다.
  - 사용 사례: 쿼리와 가장 유사한 예제를 선택하여 모델이 특정 시나리오에 대해 정확하게 학습할 수 있도록 할 때 유용합니다.
  - 특징: 예제 간의 다양성보다는 쿼리와의 유사성에 더 중점을 둡니다. 따라서 유사한 예제가 여러 개 선택될 수 있습니다.

### 요약

MaxMarginalRelevanceExampleSelector는 다양성과 관련성을 균형 있게 고려하여 예제를 선택합니다.
SemanticSimilarityExampleSelector는 주로 쿼리와의 의미적 유사성을 기준으로 예제를 선택합니다.
이 두 선택기는 사용하는 상황과 목적에 따라 적절하게 선택할 수 있습니다.
예를 들어, 다양한 시나리오를 다루는 모델을 학습시키려면 MaxMarginalRelevanceExampleSelector를 사용하고,
특정 시나리오에 대해 정확한 예측을 원한다면 SemanticSimilarityExampleSelector를 사용할 수 있습니다.

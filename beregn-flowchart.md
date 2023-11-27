```mermaid
graph TD;
    A([Init \n beregn]) -->|call calc_kcal| B(Calculate bmr)
    B --> C(Calculate bmr on activity level)
    C --> D(Return bmr)
    D --> E([End])
``` 

''''mermaid
flowchart TD
    A((Start GUI)) -->B
    B{User}
    B -->|Create|C[Create USER]
    C-->E[Save]
    E-->F{New}
    F-->|Yes|B
    F-->|No|D
    B -->|No|D{Show}
    D-->|No new info added|J
    D-->|Add new info|H{Update}
    H-->|Yes|K[Update user]
    K-->D
    H-->|No|J{Close Program}
    J-->|No|B
    J-->|Yes|I((End))

''''


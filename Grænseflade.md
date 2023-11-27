|         |   Name |  BD  |  Height   |  Weigth   |  Age  |  AMR   |  Activity   | Gender  |
|---------|--------|--------|--------|--------|--------|--------|--------|--------|
| User    |    x    |   x     |  x      |    x    |    x    |   x     |   x     |    x    |
| body    |        |        |   x     |    x    |   x     |        |   x     |  x      |

```mermaid

graph
  U[User]
  G[GUI]
  D[DB]
  C[Calculate]

  U --> |user dict| G
  U --> |user dict| D
  U --> |body dict| C
  


```

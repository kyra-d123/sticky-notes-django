# Class Diagram

```mermaid
classDiagram
    class Note {
        +CharField title
        +TextField content
        +DateTimeField created_at
        +DateTimeField updated_at
        +__str__() str
    }
```

```py
Draft
[ Presentation Layer (UI/Console) ]
               │  (Calls commands / sends inputs)
               ▼
[ Service Layer (Business Logic / AuthService) ]
               │  (Validates state / maps data models)
               ▼
[ Repository Layer (Database Access / UserRepository) ]
               │  (Executes raw SQL / File I/O)
               ▼
[ Data Layer (SQLite Database / JSON File) ]
```
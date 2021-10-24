# Демонстрационные запросы

```graphql
mutation {
    addCustomer (name: "John", email: "jJoeman@aol.com") {
        success errors 
        customer {
            id name email
        }
    }
}
```

```graphql
mutation {
    addCustomer (name: "Jeremmy", email: "jeremy118@mail.com") {
        success errors 
        customer {
            id name email
        }
    }
}
```

```graphql
mutation {
    updateCustomer (customerId: 2, name: "Jeremy", email: "jeremy1189@mail.com") {
        success errors 
        customer {
            id name email
        }
    }
}
```

```graphql
mutation {
    removeCustomer (customerId: 2) {
        success errors
    }
}
```

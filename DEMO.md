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


```graphql
mutation {
    addSeller (name: "best flower", photoUrl: "https://example.com") {
        success errors 
        seller {
            id name photoUrl dateCreated
        }
    }
}
```

```graphql
mutation {
    addSeller (name: "bad flower", photoUrl: "https://example.com") {
        success errors 
        seller {
            id name photoUrl dateCreated
        }
    }
}
```
```graphql
mutation {
    updateSeller (sellerId: 2, name: "worst flower", photoUrl: "https://example.com") {
        success errors 
        seller {
            id name photoUrl dateCreated
        }
    }
}
```
```graphql
mutation {
    removeSeller (id: 2) {
        success errors
    }
}
```

```graphql
mutation {
    addBouquet (name: "Roses", photoUrl: "https://example.com", price: 159.99, sellerId: 1) {
        success errors
        bouquet {
            id name photoUrl price
            seller {
                id name
            }
        }
    } 
}
```

```graphql
mutation {
    addBouquet (name: "Violets", photoUrl: "https://example.com", price: 1599.99, sellerId: 1) {
        success errors
        bouquet {
            id name photoUrl price
            seller {
                id name
            }
        }
    } 
}
```
```graphql
mutation {
    updateBouquet (bouquetId: 2, name: "Cool Violets", photoUrl: "https://example.com", price: 420) {
        success errors
        bouquet {
            id name photoUrl price
            seller {
                id name
            }
        }
    } 
}
```

```graphql
query {
    sellers {
        success errors
        sellers {
            id name bouquetsSold
            bouquets {
                id name price
            }
        }
    }
}
```
```graphql
query {
    bouquets {
        success errors
        bouquets {
            id name price
            seller {
                id price bouquetsSold
            }
        }
    }
}
```

```graphql
mutation {
    purchaseBouquet (bouquetId: 1, customerId: 1) {
        success errors
        purchase {
            id price commission
            bouquet {
                id name
                seller {
                    id name
                }
            }
            customer {
                id name email
            }
        }
    }
}
```
```graphql
mutation {
    purchaseBouquet (bouquetId: 2, customerId: 1) {
        success errors
        purchase {
            id price commission
            bouquet {
                id name
                seller {
                    id name
                }
            }
            customer {
                id name email
            }
        }
    }
}
```

```graphql
query {
    purchases (customerId: 1) {
        success errors
        purchases {
            id price commission
            bouquet {
                id name
                seller {
                    id name
                }
            }
            customer {
                id name email
            }

        }
    }
}
```

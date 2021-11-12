# POS - cli - instructions

```cmd
init collection
```

## User

### Login

```
user login <username>
```

### View User

```
user get
```

## Customer

### Create

```cmd
customer add <name> <address> <phone>
```

### All

```cmd
customer all
```

### View

```cmd
customer find <id>
```

### Search

```cmd
customer search <key> <value>
```

## Item

### add item

```cmd
item add <name> <price> <selling_price>
```

### get all item

```cmd
item all
```

### find by Id

```cmd
item find <id>
```

### Search Items

```cmd
item search <key> <value>
```

## Order

### place order

```cmd
order place <customerId> <itemId> <itemPrice> <itemQty>
```

### get all orders

```cmd
order all
```

### find order

```cmd
order find <id>
```


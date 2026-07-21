# DAX Measures - Week 3 Day 2

## 1. Average Academic Performance

```DAX
Average Academic Performance =
AVERAGE(teen_phone_addiction_dataset[Academic_Performance])
```

## 2. High Academic Performance

```DAX
High Academic Performance =
CALCULATE(
    AVERAGE(teen_phone_addiction_dataset[Academic_Performance]),
    teen_phone_addiction_dataset[Academic_Performance] >= 75
)
```

## 3. Average Self Esteem

```DAX
Average Self Esteem =
AVERAGE(teen_phone_addiction_dataset[Self_Esteem])
```

## 4. Average Anxiety Level

```DAX
Average Anxiety Level =
AVERAGE(teen_phone_addiction_dataset[Anxiety_Level])
```

## 5. Average Depression Level

```DAX
Average Depression Level =
AVERAGE(teen_phone_addiction_dataset[Depression_Level])
```

## Row Context

- Used in Calculated Columns.
- Calculates one row at a time.
- Example: Self Esteem Percentage.

## Filter Context

- Used in Measures.
- Changes calculations based on filters.
- Example: High Academic Performance using CALCULATE().

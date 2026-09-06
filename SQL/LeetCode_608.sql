WITH Relation AS (
    SELECT Parent.id AS ParentId, Middle.id AS id, Child.id AS ChildId
    FROM Tree AS Parent
    RIGHT JOIN Tree AS Middle ON Parent.id = Middle.p_id
    LEFT JOIN Tree AS Child ON Middle.id = Child.p_id
),
Leafs AS (
    SELECT DISTINCT id, "Leaf" AS `type`
    FROM Relation
    WHERE ChildId IS NULL AND ParentId IS NOT NULL
),
Roots AS (
    SELECT DISTINCT id, "Root" AS `type`
    FROM Relation
    WHERE ParentId IS NULL
),
Inners AS (
   SELECT DISTINCT id, "Inner" AS `type`
   FROM Relation
   WHERE ChildId IS NOT NULL AND ParentId IS NOT NULL
),
Results AS (
    SELECT * FROM Leafs
    UNION
    SELECT * FROM Roots
    UNION
    SELECT * FROM Inners
)
SELECT * FROM Results

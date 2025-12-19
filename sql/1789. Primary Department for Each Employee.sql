WITH ranked AS (
  SELECT
    employee_id,
    department_id,
    primary_flag,
    COUNT(*) OVER (PARTITION BY employee_id) AS dept_cnt,
    ROW_NUMBER() OVER (
      PARTITION BY employee_id
      ORDER BY (primary_flag = 'Y') DESC, department_id
    ) AS rn
  FROM Employee
)
SELECT employee_id, department_id
FROM ranked
WHERE (dept_cnt = 1 AND rn = 1)      -- only one department -> pick it
   OR (dept_cnt > 1 AND rn = 1);     -- multiple departments -> 'Y' will be ranked first

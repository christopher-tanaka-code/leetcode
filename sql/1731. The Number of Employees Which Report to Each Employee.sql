SELECT
    m.employee_id,
    m.name,
    COUNT(*) AS reports_count,
    ROUND(AVG(e.age), 0) AS average_age
FROM Employees e
JOIN Employees m
  ON e.reports_to = m.employee_id          -- e = direct report, m = manager
GROUP BY
    m.employee_id,
    m.name
ORDER BY
    m.employee_id;

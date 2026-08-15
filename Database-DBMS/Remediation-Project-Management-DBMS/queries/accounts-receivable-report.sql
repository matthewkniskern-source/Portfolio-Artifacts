-- Accounts-receivable reporting query
-- Returns completed projects that remain unpaid after 30 days,
-- including customer and assigned primary PM contact information.

SELECT
    p.JobID,
    p.ProjectDetails,
    p.CompletionDate,
    ps.Paid_30,
    c.BusinessName AS CustomerName,
    c.PrimaryPOCName,
    c.POCRole AS CustomerPOCRole,
    c.ContactInfo AS CustomerPOCContact,
    e.Name AS AssignedPM,
    e.ContactInfo AS PMContact
FROM projects p
JOIN paymentstatus ps
    ON p.JobID = ps.JobID
JOIN customers c
    ON p.CustomerID = c.CustomerID
JOIN project_assigned_pms pap
    ON p.JobID = pap.ProjectID
    AND pap.Role = 'Primary'
JOIN employees e
    ON pap.EmployeeID = e.EmployeeID
WHERE ps.Paid_30 = 0
  AND p.CompletionDate < CURDATE() - INTERVAL 30 DAY;

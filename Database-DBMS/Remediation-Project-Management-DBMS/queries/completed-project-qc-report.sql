-- Completed-project / quality-control reporting query
-- Shows all completed projects, including projects with no inspection record,
-- with customer and primary PM details.

SELECT
    p.JobID,
    p.ProjectDetails,
    p.CompletionDate,
    qc.InspectionDate,
    qc.IssuesFound,
    qc.Resolutions,
    qc.FinalApproval,
    c.BusinessName AS Customer,
    e.Name AS AssignedPM,
    e.ContactInfo AS PMContact
FROM projects p
LEFT JOIN qualitycontrol qc
    ON p.JobID = qc.JobID
LEFT JOIN customers c
    ON p.CustomerID = c.CustomerID
LEFT JOIN project_assigned_pms pap
    ON p.JobID = pap.ProjectID
    AND pap.Role = 'Primary'
LEFT JOIN employees e
    ON pap.EmployeeID = e.EmployeeID
WHERE p.CompletionDate IS NOT NULL
ORDER BY p.CompletionDate DESC;

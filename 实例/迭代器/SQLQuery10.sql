--select count(*) from DimDate
--select count(*) from DimObject
--select count(*) from DimSubject
--select count(*) from FactEvent

--SELECT  ROW_NUMBER() OVER( ORDER BY Subject) as ID, Subject AS SubjectName
--FROM    dbo.Event
--group by Subject

--SELECT  ROW_NUMBER() OVER( ORDER BY Object) as ObjectID, Object AS ObjectName
--FROM    dbo.Event
--group by Object

--SELECT        dbo.DimDate.DateKey, dbo.DimObject.ObjectID, dbo.DimSubject.SubjectID, dbo.Event.Location, dbo.Event.Event, dbo.Event.Cost, dbo.Event.AMPM
--FROM            dbo.Event INNER JOIN
--                dbo.DimDate INNER JOIN
--                dbo.DimObject INNER JOIN
--                dbo.DimSubject
--ON CAST(CONVERT(varchar(8), dbo.Event.Date, 112) AS INT) = dbo.DimDate.DateKey

--SELECT        dbo.DimObject.ObjectID, dbo.DimSubject.SubjectID, dbo.DimDate.DateKey, dbo.Event.Event, dbo.Event.Location, dbo.Event.Cost, dbo.Event.ID
--FROM            dbo.Event INNER JOIN
--                dbo.DimDate ON CONVERT(varchar(8), dbo.Event.Date, 112) = dbo.DimDate.DateKey INNER JOIN
--                dbo.DimObject ON dbo.Event.Object = dbo.DimObject.ObjectName INNER JOIN
--                dbo.DimSubject ON dbo.Event.Subject = dbo.DimSubject.SubjectName

select * from FactEvent

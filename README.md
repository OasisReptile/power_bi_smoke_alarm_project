**Business Scenario**

It has been discovered that a lot of properties the business manages may have missing or faulty smoke alarms. As such, teams were sent out to check the alarms, the outcome of which has been displayed in a Power BI dashboard.

The primary function of the dashboard is to show the repairs team which properties need to have follow up work, and to enable the team leaders to capture that data in the dashboard itself.

The dashboard writeback is a relatively new functionality, powered by Microsoft Fabrtic tools such as translytical flows and Fabric SQL database. This opens up a world of possibilities, as up to this point, the only way to implement writeback was through Power Apps integrations, which had huge licensing costs. The new technique reduces cost, is easier to implement, manage and track changes, while also being more flexible.

The first dashboard page shows what action the users need to take, that is to schedule and input the Job ID, so that the smoke alarm issue can be addressed as soon as possible.
<img width="1422" height="799" alt="image" src="https://github.com/user-attachments/assets/1dbe635c-b6ed-4de6-b2af-f300fc758cc9" />

The next page shows a general overview, so that the user can understand the progress of the project, the scale of the issue and how the business is addressing it.
<img width="1413" height="792" alt="image" src="https://github.com/user-attachments/assets/134ce74c-d14d-4e8b-a13b-e683eb513b74" />

There is also a data extract page, with instructions to show how to export the data for further analysis, as well as filters to only show relevant data.
<img width="1425" height="797" alt="image" src="https://github.com/user-attachments/assets/3ebfb652-59a7-44a4-8b28-c55e60d49db0" />

The dashboard is built using a standard star schema, though in real world dashboards the models get much more complex, often with multiple fact tables and external data sources for further analysis.
<img width="869" height="724" alt="image" src="https://github.com/user-attachments/assets/129da58d-1dbe-4932-8de7-95a053935cc2" />

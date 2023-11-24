from django.db import models

class Employee(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.TextField(null=True)
    Email = models.EmailField(unique=True, null=True)
    EmpNo = models.TextField(unique=True, null=True)
    SupervisorID = models.ForeignKey('Supervisor', on_delete=models.SET_NULL, null=True)
    ReliefID = models.ForeignKey('Relief', on_delete=models.SET_NULL, null=True)
    UnitID = models.ForeignKey('Unit', on_delete=models.SET_NULL, null=True)
    SubUnitID = models.ForeignKey('SubUnit', on_delete=models.SET_NULL, null=True)
    StatusID = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    EmployeeReliefRecord = models.TextField('Relief',on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.Name} - {self.Email}"


class Supervisor(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.TextField(null=True)
    Email = models.TextField(unique=True, null=True)

    def __str__(self):
        return f"{self.Name} - {self.Email}"

class Relief(models.Model):
    ID = models.AutoField(primary_key=True)
    EmpID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)  
    ReleifID = models.ForeignKey('Unit', on_delete=models.CASCADE, null=True)  
    StatusID = models.ForeignKey('Status', on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return f"Relief ID: {self.ID}, Employee ID: {self.EmpID}, Unit ID: {self.ReleifID}, Status ID: {self.StatusID}"


class Unit(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.TextField(null=True)

    def __str__(self):
        return f"Unit ID: {self.ID}, Name: {self.Name}"


class SubUnit(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.TextField(null=True)
    Unit = models.ForeignKey('Unit', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Sub-unit ID: {self.ID}, Name: {self.Name}, Unit ID: {self.UnitID}"


class Leave(models.Model):
    ID = models.AutoField(primary_key=True)
    EmpID = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True)
    StartDate = models.DateField(null=True)
    EndDate = models.DateField(null=True)
    Status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True)
    TotalNoDays = models.IntegerField(null=True)
    DaysTaken = models.IntegerField(null=True)
    DaysRemaining = models.IntegerField(null=True)
    LeaveTypeID = models.ForeignKey('LeaveType', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'ID: {self.ID}, StartDate: {self.StartDate}, EndDate: {self.EndDate}, Status: {self.Status}, TotalNoDays: {self.TotalNoDays}, LeaveTypeID: {self.LeaveTypeID}'


class LeaveType(models.Model):
    ID = models.AutoField(primary_key=True)
    LeaveType_Choices = [
        ('ANNUAL', 'Annual'),
        ('COMPASSIONATE', 'Compassionate'),
        ('STUDY', 'Study'),
    ]
    LeaveType = models.CharField(max_length=255, null=True,Choices=LeaveType_Choices,default='ANNUAL',
    )
    TotalNoDays = models.IntegerField(null=True)

    def __str__(self):
        return f'ID: {self.ID}, LeaveType: {self.LeaveType}, TotalNoDays: {self.TotalNoDays}'
    

class Status(models.Model):
    ID = models.AutoField(primary_key=True)
    StatusType_Choices = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('APPROVE', 'Approve'),
        ('PENDING', 'Pending'),
        ('DECLINE', 'Decline'),
    ]
    StatusType = models.CharField(max_length=255, null=True,Choices=StatusType_Choices,default='ACTIVE',
    )

    def __str__(self):
        return f'ID: {self.ID}, StatusType: {self.StatusType}'


class EngagementManager(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.TextField(null=True)
    Email = models.EmailField(unique=True, null=True)

    def __str__(self):
        return f'ID: {self.ID}, Name: {self.Name}, Email: {self.Email}'       






        
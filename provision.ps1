#Global Variables
$project = "norcom911"
$zone = "us-east4-a"
#VPC

$networkname = "server-vpc"

New-GceNetwork $networkname -AutoSubnet

#Firewall Rules
$firewallname = "server-firewall"

New-GceFirewallProtocol tcp -Port 80, 443, 3389, 22 | 
New-GceFirewallProtocol icmp | 
Add-GceFirewall -Project $project -Name $firewallname

#Compute Engine
$instancename = "instance-uno"
$disk = Get-GceImage "windows-cloud" -Family "windows-2019"
$config = New-GceInstanceConfig $instancename `
    -MachineType "e2-medium" `
    -DiskImage $disk `
    -Network $networkname 

$config | Add-GceInstance -Project $project -Zone $zone
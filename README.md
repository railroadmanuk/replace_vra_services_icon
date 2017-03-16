# Replace vRA 'All Services' icon
## Overview
This script replaces the vRealize Automation 7.1+ 'All Services' icon with a .png file of your choosing.
## Pre-requisites
Place the .png file you are using in the same folder as the script, and edit the following lines:
```python
# replace these variables
filename = 'service.png'
vra_ip = '192.168.1.227'
vra_user = 'administrator@vsphere.local'
vra_pass = 'VMware1!'
vra_tenant = 'vsphere.local'
```
You will need the 'requests' Python package. This can be installed using pip.
## Future enhancements
* Writing a script to delete the custom icon, restoring the original lego brick, this is present here but does not work at this time

## References
Used the following documents to create this:
* http://www.justait.net/2016/09/vRA-change-all-services.html
* https://pubs.vmware.com/vrealize-automation-72/topic/com.vmware.ICbase/PDF/vrealize-automation-72-management.pdf#page40

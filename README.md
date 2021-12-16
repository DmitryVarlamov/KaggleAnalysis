# KaggleAnalysis
University project of Kaggle dashboards and competitions analysis

## ELK installation guide
This is the list of steps you need to make in order to deploy ELK stack on your machine

[There is a video guide that you can use to help you to install ELK stack](https://vk.com/video-206875300_456239020?list=5be6707e93a2c992e5) 

1. Download this repository.

2. Install Ansible on your machine (This can either be machine where you want to deploy ELK stack or separate machine).

3. Add information about your host where you want to deploy ELK stack to inventory.txt file. Fields that need to be fulfilled: ansible_ssh_pass, ansible_user and ansible_host. If you want to deploy multinode cluster, add all hosts in separate lines.

4. Launch playbook with "ansible-playbook -i inventory.txt deploy_elk.yaml" command

5. If you want to use already created preset of dashboards, then after the cluster is deployed go to <your_ip>:5601/app/management/kibana/objects endpoint and click "import". Then choose "kibana_export.ndjson" file that is located in "exports" folder of this repository.

6. To upload new data to elasticsearch, launch connector script with "python kaggle_api.py" command
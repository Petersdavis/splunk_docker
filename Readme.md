STEPS TO SET UP SPLUNK AND POLING OF CLOUDFLARE:

1) #docker-compose up
--Once it is fully up Splunk should be available on port 8000
--Login using uname:"admin"  pwd:"{{SPLUNK_PASSWORD}}"   
TODO: rm SPLUNK_PASSWORD from docker-compose.yml and create secret

2) Setup Http Event Collector
--In the Main Window click Settings=>Data inputs
--Add a New HTTP Event Collector
--Specify name: "cloudflare"  click: Next
--Input settings: automatic  Index: Create a new index named "cloudflare"  <==this is the bucket your data goes in.
--Select the new index "cloudflare" click: Review
--click: Submit
copy the TOKEN on this page
--In the Main Menu click Settings=>Data inputs again
--Click on Http Event Collectors (should now show "cloudflare")
--Click on Global Settings ==>  Click All Tokens => Enabled
--Also verify that port:8088 and ssl:enabled

At this point you should be able to send data to splunk:
curl -k https://<CONTAINER_IP>:8088/services/collector/event/1.0 -H "Authorization: Splunk <TOKEN>" -d '{"event": "hello world"}'


3) Configure Python Container
--in python/docker-compose.yml
--set:
splunk-token: <<YOUR TOKEN>>
splunk-url: "https://<<EXTERNAL IP OF SPLUNK>>:8088"

--set desired parameters for cloudflare api in python/cloudflare/cloudflare.py
--run docker-compose up

4) Verify Data is being loaded correctly.
--in Splunk browser click Apps=> Search & Reporting
--search index="cloudflare" 











    
    

    


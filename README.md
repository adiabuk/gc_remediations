# gc_remediations
Greencandle StackStorm remediation

Install instructions:
* ensure password in htpassword matches  files/st2-cli.conf
* ensure st2service_handler.yaml in nagios contains correct api token from docker compose file or .env file
* ensure you can reach st2 api on http://<host>/api/v1/triggertypes/nagios.service_state_change
* ensure st2-docker-st2web-1 is running
* connect to client container: docker exec -it st2-docker-st2client-1 bash
* st2 pack install nagios
* st2 pack install https://github.com/adiabuk/gc_remediations.git
* Trigger event either from nsca to nagios, or /opt/nagios_checks/st2service_handler.py from nagios
`/opt/nagios_checks/st2service_handler.py /opt/nagios/etc/st2service_handler.yaml 12345 "Stream API 1d" "CRITICAL" "3" "HARD" "4" "<ip of service>"`
* check output and entry in st2 UI (triggers=>nagios=> instances and history tab
* check rule in UI (Rules=>GC REMEDIATIONS =>Risk trigger=> ENFORCEMENTS
* Check actions in UI (Actions =>GC REMEDIATIONS=>check_risk=>ENFORCEMENTS

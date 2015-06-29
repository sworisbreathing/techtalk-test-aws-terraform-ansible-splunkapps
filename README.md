# Apps for Splunk+AWS+Terraform+Ansible Tech Talk

This repository contains the splunk apps used in the live demo for the tech talk on testing upgrade paths in Splunk using AWS, Terraform, and Ansible.

These apps have been pulled from the customer's repository and the customer's IP removed. What you will find in this repository are a subset of the actual apps we did for this customer (pretty much just the off-the-shelf apps from Splunkbase).

## Branches

### master

The `master` branch simply contains this README file. You won't find any apps here.

### old-deployment-strategy

This branch contains the apps as they were structured and deployed when we began the engagement. Each app bundle contains not only the user-facing components (e.g. dashboards, saved searches, et cetera), but the `inputs.conf` for reading the log files as well. The folder structure looked a bit like this:

    /app/git/splunk-deployment-apps/
      custom_app_1/
      custom_app_2/
      ...
      custom_app_n/
      dashboard_examples/
      splunk_license_usage/
      Splunk_SA_ONTAP_KB/
      Splunk_TA_ONTAP7/
      SplunkAppForNetAppONTAP/
      sos/
      sideview_utils/
      TA-sos/
      unix/

The deployment process for these apps was simply to pull down the apps from git into `/app/git/splunk-deployment-apps` (which the Splunk deployment server is configured to use in lieu of `$SPLUNK_HOME/etc/deployment-apps`) and then copy them all into `$SPLUNK_HOME/etc/apps` on the standalone Splunk server, then restart the Splunk server.

This branch does not contain `serverclass.conf`, since under the old deployment strategy it was versioned in the configuration management repository.

### new-deployment-strategy

This branch contains the apps as we left them at the end of the engagement. All apps, even the off-the-shelf ones from Splunkbase, were split into apps (installed on the Splunk server) and TAs (deployed to forwarders). The folder structure now looks like this:

    /app/git/splunk-deployment-apps/
      apps/
        custom_app_1/
        custom_app_2/
        ...
        custom_app_n/
        dashboard_examples/
        splunk_license_usage/
        Splunk_SA_ONTAP_KB/
        SplunkAppForNetAppONTAP/
        Splunk_TA_ONTAP7/
        sos/
        sideview_utils/
        TA-sos/
        unix/
      deployment-apps/
        custom_TA_1/
        custom_TA_2/
        ...
        custom_TA_n/
        TA-sos/
        TA-unix/
      serverclass.conf

The deployment process for these apps is to pull the apps down from git into `/app/git/splunk-deployment-apps` as before. Only now, the apps deployed to forwarders are in one subfolder, and the apps installed on the Splunk server are in another subfolder. There is a custom script (in the configuration management repository) to determine if the Splunk server really needs to be restarted, or if we can get by with just calling `splunk reload deploy-server` instead.

# Haraj Auto Ad Updater
 Updates an Ad on each run.

## Requirements
```
pip install -r requirements.txt
```

## Configurations
Configs in this program are limited to three, the first two, Auth and PostId are needed to be able to update the correct post with the owner's auth token to be privliged for such request. And the last configuration is "English", which specifies if you want the logs being printed be printed in Arabic or English, this option is available because you've the option to from the website itself, and also primarly because the Windows terminal is incapable of rendering Arabic unicode, thus English option exists for log-purposes.

Finally, keep in mind that you need to cut the last far left two digits from most post ids, and you can get post id from the url, or preferably the network tab, and don't forget to schedule the program to run every 23ish hour or so. Now enjoy the advantage!

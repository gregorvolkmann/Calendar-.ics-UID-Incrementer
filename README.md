# Calendar-.ics-UID-Incrementer
Alter your exported Calendars so Calendar Server handles the containing events as new ones.

To restore deleted Calendars from TimeMachineBackup:
* Go to /Users/USERNAME/Library/Calendars/ and restore ALL files from this folder to your harddrive (e.g. RESTOREDCALENDAR).
* GO OFFLINE
* CLOSE Apple iCal

Sometimes CalendarAgent restarts very fast, therefore run the following three lines in shell (moves restore calendars to library folders)

```
killall CalendarAgent
# WARNING deletes all your calendars!
rm -Rf /Users/Gregor/Library/Calendars/*
mv /RESTOREDCALENDAR/* /Users/Gregor/Library/Calendars/
```

* START iCal
* EXPORT your calendars you want to restore
* GO ONLINE (iCal syncs your restored, but earlier deleted calendars away
* Use the incrementer on your exported calendars
* import incremented calendars.ics

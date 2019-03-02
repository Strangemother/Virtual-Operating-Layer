# Quite Time Cleaner

The Quiet Time Cleaner will delete old imports, ram cache and general live data
imports. As the application works it will gradually populate FS graphs and import
caches.
Based upon scheduling of applications through the core thread, the GC will run
when no other app is currently using CPU time. If a softheader is reached within
the _sleep_ time - a light cleaner is applied, keeping costs as a minimum.

If the RAM, FS, Imports etc hit a hard peek; the subst is frozen for a hardclean
- of which is just a _standard_ GC cleanup. Hopefully this will utilize
power a bit more efficiently.

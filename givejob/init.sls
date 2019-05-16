/home/worker/jobs/jobi:
   file.managed:  
     - source: salt://job.py

run_jobi:
  cmd.run:
    - user: root
    - cwd: /home/worker/jobs
    - name: sudo python3 jobi

# Tutoring backend

## To-do

- [ ] VIEW ON SITE on admin page.
- [ ] API testing code
- [ ] Add website_alert, display info on the top of the website
- [x] Change feedback to contact_us
- [x] Cancel pagination for meetings api
- [x] Change SQLite to PostgreSQL
- [x] Auto renew letsencrypt
- [ ] BMCC CUNYfirst_ID, null=False
- [ ] Zoom link on Admin
- [ ] Registration number limit, waitlist
- [ ] User can change password, profile
- [ ] Add is_expire function as a field
- [ ] Add duration field (meeting_start_time, meeting_end_time)
- [ ] Admin time HH:MM instead of HH:MM:ss
- [ ] Display AM/PM
- [x] Remove email case sensitive for Admin login.
- [ ] Hide IP address using nginx
- [ ] Evaluation for tutors
- [ ] On Admin - Meeting list page, display is_active icon
- [ ] On Admin - Meeting detail page, highlight is_active option

## Run locally

1. Install Python (>=3.8)

2. Create and activate a Python virtual environment
   ```bash
   $ cd /path/to/tutoring/backend
   $ python3 -m venv .venv     # Create a virtual env
   $ source .venv/bin/activate # Activate a virtual env
   ```
   
3. Install dependencies
   ```bash
   (.venv) $ pip install -r backend/requirements.txt
   ```

4. Install and config PostgreSQL
   Refernce: [Config PostgreSQL for Django on Ubuntu](https://github.com/Qingquan-Li/blog/issues/230)

5. Apply migrations to database
   ```bash
   (.venv) $ python manage.py migrate --settings=a_project_config.settings.local
   ```

6. Create a `.env` (stores environment variables) file in the root of the backend folder.
   The `.env` file content:
   ```
   SECRET_KEY=Your Django Secret Key
   LOCAL_POSTGRESQL_PASSWORD=Your PostgreSQL Password
   ```

7. Run the backend project
   ```bash
   (.venv) $ python manage.py runserver 0:8000 --settings=a_project_config.settings.local
   ```

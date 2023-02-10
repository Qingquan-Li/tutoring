# Tutoring backend

## To-do

- [x] Testing
- [x] favicon.ico
https://www.helpyourmath.com/images/img/logo1.jpg
- [x] On RegistrationAdmin, add filter on the right side.
- [x] On tutor end's, show number of registrations.
- [ ] Deploy on cloud sever.
- [ ] VIEW ON SITE on admin page.
- [x] API
- [ ] API test code
- [ ] Add website_alert, display info on the top of the website
- [x] Change feedback to contact_us
- [x] Add `verbose_name='Detail (tell more about this meeting)'` to `summary` field
- [x] Add field `introduction` field, `verbose_name='Introduce yourself (optional)'` to profile
- [x] Cancel pagination for meetings api
- [ ] Change SQLite to PostgreSQL
- [ ] Auto renew letsencrypt
- [ ] BMCC CUNYfirst_ID, null=False
- [ ] Zoom link on Admin
- [ ] Registration number limit, waitlist
- [ ] User can change password, profile
- [ ] Add is_expire function as a field
- [ ] Add duration field
- [ ] Admin time HH:MM instead of HH:MM:ss
- [ ] Display AM/PM
- [x] Remove email case sensitive for Admin login.
- [ ] Hide IP address using nginx
- [ ] Evaluation for tutors
- [ ] Move the deploy folder to the root directory

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

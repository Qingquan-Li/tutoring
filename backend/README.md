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

## Run locally

```bash
$ cd backend && source .venv/bin/activate
$ python manage.py runserver 0:8000 --settings=a_project_config.settings.local
```

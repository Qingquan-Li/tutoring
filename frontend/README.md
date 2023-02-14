# Tutoring frontend

## Todo:

- [ ] Check my registration through email address
- [ ] Search tutoring session (via `subject` field)
- [ ] Filter sessions by `date`, `way` fiedds
- [ ] On meeting detail page, if `!is_active` then 404;
- [ ] if `meeting_time < current_time` then Can not register (disable the form)
- [ ] Display tutors' email
- [ ] Add favicon.ico
- [ ] Home page sort by meeting time
- [ ] Add boolean is_expire function field
- [ ] Add duration field (meeting_start_time, meeting_end_time)
- [ ] admin time HH:MM, not second
- [ ] 24-hour clock to 12-hour clock (AM/PM)
- [ ] Distinguish title: tutor/professor...
- [ ] Navigate to a new page to notify "Registration successful" after registering the form

## Run in the development mode

```bash
$ cd frontend && npm start
```

## Before pushing the code to GitHub (creating pull requests)

If you have changed the RootAPIURL in the `frontend/src/common/RootAPIURL.js` file,
before pushing the code, change the Local RootAPIURL to Production RootAPIURL.

## Build for production

If you have changed the RootAPIURL in the `frontend/src/common/RootAPIURL.js` file,
before pushing the code, change the Local RootAPIURL to Production RootAPIURL.

```bash
$ npm run build
```

## SCP build folder to the server

```bash
$ scp -r build username@server_ip:/home/jake/tutoring/frontend
```

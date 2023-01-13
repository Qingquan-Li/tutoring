# Tutoring frontend

## Todo:

- [x] Configure React environment
- [ ] React Router
- [x] Bootstrap
- [ ] Deploy front-end project
    - https://create-react-app.dev/docs/deployment/
    - https://pages.cloudflare.com/
    - https://www.digitalocean.com/community/tutorials/how-to-deploy-a-react-application-with-nginx-on-ubuntu-20-04
- [ ] Meeting list page
- [ ] Meeting detail and registration page
- [ ] Check my registration through email address
- [ ] Search tutoring session (via `subject` field)
- [ ] Filter sessions by `date`, `way` fiedds
- [ ] Can not register if `!is_active || meeting_time < (current_time + 2hours)`
- [ ] Display tutors' email
- [ ] favicon.ico
- [ ] Home page sort by meeting time
- [ ] URL parameter with id
- [ ] Add boolean is_expire function field
- [ ] Add duration field
- [ ] admin time HH:MM, not second
- [ ] 24-hour clock to 12-hour clock (AM/PM)
- [ ] comment/text tutor
- [ ] Distinguish title: tutor/professor...

## Run in the development mode

```bash
$ cd frontend && npm start
```

## Build for production

```bash
$ npm run build
```

## SCP build folder to the server

```bash
$ scp -r build username@server_ip:/home/jake/tutoring/frontend
```

# Tutoring frontend

## Todo:

- [ ] Search tutoring session (via `subject` field)
- [ ] Filter sessions by `date`, `way` fiedds
- [ ] On meeting detail page, if `!is_active` then 404;
- [ ] Display tutors' email
- [ ] Add favicon.ico
- [ ] Add duration field (meeting_start_time, meeting_end_time)
- [ ] admin time HH:MM, not second
- [ ] Distinguish title: tutor/professor...
- [ ] Navigate to a new page to notify "Registration successful" after registering the form
- [ ] Create testing code for React

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

### Build locally
```bash
$ npm run build
```

### Build with GitHub Actions

1. Automatically build the react app with GitHub Actions
2. Download the `build` folder from GitHub Actions
3. Preview the `build` locally
   ```bash
   $ serve -s /path/to/build
   ```

## SCP the build folder to the server

```bash
$ scp -r build username@server_ip:/home/jake/tutoring/frontend
```

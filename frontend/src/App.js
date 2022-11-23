import {
  createBrowserRouter,
  RouterProvider,
} from 'react-router-dom';

import NavBar from './common/NavBar';
import Home from './home';
import ErrorPage from './common/ErrorPage';
import MeetingDetail from './meeting-detail';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
    errorElement: <ErrorPage />,
  },
  {
    path: '/meetings/:meetingId',
    element: <MeetingDetail />,
    errorElement: <ErrorPage />,
  },
]);

function App() {
  return (
    <>
      <NavBar />
      <RouterProvider router={router} />
    </>
  );
}

export default App;

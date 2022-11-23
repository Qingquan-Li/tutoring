import { useRouteError } from "react-router-dom";

export default function ErrorPage() {
  const error = useRouteError();
  console.error(error);

  return (
    <div style={{ textAlign: 'center', marginTop: '100px', }}>
      {error.statusText === 'Not Found' ? (
        <>
          <h1>404 Not Found</h1>
          <p>The requested URL was not found on the server.</p>
        </>
      ) : (
        <>
          <h1>Oops!</h1>
          <p>Sorry, an unexpected error has occurred.</p>
          <p>
            <i>{error.statusText || error.message}</i>
          </p>
        </>
      )}
    </div>
  );
}

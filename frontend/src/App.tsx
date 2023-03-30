import React from 'react';
import { RouterProvider, Route, defer, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';
import '@/style/default.scss';
import NotFound from './views/NotFound';
import SignIn from './views/SignIn';
import Dashboard from './views/Dashboard';
import { ProtectedLayout } from './components/ProtectedLayout';
import { HomeLayout } from './components/HomeLayout';
import { AuthLayout } from './components/AuthLayout';

const getUserData = () =>
  new Promise((resolve) =>
    setTimeout(() => {
      const user = window.localStorage.getItem('user');
      resolve(user);
    }, 3000)
  );

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route element={<AuthLayout />} loader={() => defer({ userPromise: getUserData() })}>
      <Route path="*" element={<NotFound />} />
      <Route element={<HomeLayout />}>
        <Route path="/" element={<SignIn />} />
      </Route>

      <Route path="/" element={<ProtectedLayout />}>
        <Route path="dashboard" element={<Dashboard />} />
      </Route>
    </Route>
  )
);
const App: React.FC = () => {
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
};

export default App;

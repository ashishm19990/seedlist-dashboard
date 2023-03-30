import { Navigate, useOutlet } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import { AppHeader } from './AppHeader';

export const ProtectedLayout = () => {
  const { user } = useAuth();
  const outlet = useOutlet();

  if (!user) {
    return <Navigate to="/" />;
  }

  return (
    <>
      <AppHeader pages={[{ label: 'Dashboard', path: 'dashboard' }]} />
      {outlet}
    </>
  );
};

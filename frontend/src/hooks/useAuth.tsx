import { createContext, useContext, useMemo } from 'react';
import { useNavigate } from 'react-router-dom';
import { useLazyQuery } from '@apollo/client';
import { useLocalStorage } from './useLocalStorage';
import { SEED_ADMIN_ME } from '../gql/Queries';

const AuthContext = createContext();

export const AuthProvider = ({ children, userData }) => {
  const [user, setUser] = useLocalStorage('user', userData);
  const [token, setToken] = useLocalStorage('token', null);
  const [fetchUser] = useLazyQuery(SEED_ADMIN_ME, {
    onCompleted: (data) => {
      setUser(data.me);
    },
    onError: (data) => {
      console.log(data);
      logout();
    },
  });
  const navigate = useNavigate();

  const login = async (data) => {
    setToken(data.token);
    fetchUser();
    navigate('/dashboard', { replace: true });
  };

  const logout = () => {
    setUser(null);
    setToken(null);
    navigate('/', { replace: true });
  };

  const value = useMemo(
    () => ({
      user,
      token,
      login,
      logout,
    }),
    [user]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  return useContext(AuthContext);
};

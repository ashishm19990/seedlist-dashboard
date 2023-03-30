import { gql } from '@apollo/client';

export const SEED_ADMIN_LOGIN_MUTATION = gql`
  mutation SeedsAdminLogin($username: String!, $password: String!) {
    seedsAdminLogin(username: $username, password: $password) {
      token
      user {
        id
        firstname
        lastname
      }
    }
  }
`;

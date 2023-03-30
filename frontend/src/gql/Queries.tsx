import { gql } from '@apollo/client';

export const SEED_ADMIN_ME = gql`
  query {
    me {
      id
      email
      firstname
      lastname
      clientId
    }
  }
`;

export const SEED_ISPS = gql`
  query {
    isps(enabled: 1) {
      id
      name
    }
  }
`;

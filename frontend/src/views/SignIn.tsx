import React from 'react';
import { LoadingButton } from '@mui/lab';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import { FormHelperText, Alert } from '@mui/material';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import { useMutation } from '@apollo/client';
import { useForm } from 'react-hook-form';
import { useAuth } from '../hooks/useAuth';
import { SEED_ADMIN_LOGIN_MUTATION } from '../gql/Mutations';

export default function SignIn() {
  const [isFormSubmitted, setIsFormSubmitted] = React.useState(false);
  const [formErrorMessage, setFormErrorMessage] = React.useState(null);
  const { login } = useAuth();

  const [seedsAdminLogin] = useMutation(SEED_ADMIN_LOGIN_MUTATION, {
    onCompleted: (data) => {
      setIsFormSubmitted(false);
      login(data.seedsAdminLogin);
    },
    onError: (data) => {
      setIsFormSubmitted(false);
      setFormErrorMessage(data.message);
    },
  });

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onformSubmit = (formData: React.MouseEvent<HTMLElement>) => {
    setFormErrorMessage(null);
    setIsFormSubmitted(true);
    seedsAdminLogin({
      variables: {
        username: formData.email,
        password: formData.password,
      },
    });
  };

  return (
    <Container
      maxWidth="false"
      className="signin-box h-100"
      sx={{
        display: 'flex',
        alignItems: 'center',
      }}
    >
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box>
          <img src={process.env.INBOXABLE_LOGO_URL} style={{ width: 100 + '%' }} />
        </Box>

        <Box
          className="signin-form-box"
          sx={{
            padding: 2,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Box component="form" onSubmit={handleSubmit(onformSubmit)} noValidate sx={{ mt: 1 }}>
            <TextField
              disabled={isFormSubmitted}
              margin="normal"
              className="form-control"
              error={errors.email ? true : false}
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              autoFocus
              {...register('email', { required: true })}
            />
            {errors.email?.type === 'required' && (
              <FormHelperText error={true} component="span">
                This field is required
              </FormHelperText>
            )}
            <TextField
              disabled={isFormSubmitted}
              margin="normal"
              error={errors.password ? true : false}
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
              {...register('password', { required: true })}
            />

            {errors.password && (
              <FormHelperText error={true} component="span">
                This field is required
              </FormHelperText>
            )}
            {formErrorMessage && <Alert severity="error">{formErrorMessage}</Alert>}
            <LoadingButton type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }} loading={isFormSubmitted}>
              Sign In
            </LoadingButton>
          </Box>
        </Box>
      </Container>
    </Container>
  );
}

import { Box, Container, Typography, Button } from '@mui/material';
import { Link } from 'react-router-dom';

export default function NotFound() {
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
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            flexDirection: 'column',
            minHeight: '100vh',
          }}
        >
          <Typography variant="h1" style={{ color: 'white' }}>
            404
          </Typography>
          <Typography variant="h6" style={{ color: 'white' }} sx={{ mb: 1 }}>
            The page you’re looking for doesn’t exist.
          </Typography>
          <Link to="/">
            <Button variant="contained">Go Back</Button>
          </Link>
        </Box>
      </Container>
    </Container>
  );
}

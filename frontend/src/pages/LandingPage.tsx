import { Button, Container, Stack, Typography } from '@mui/material';
import { Link } from 'react-router-dom';

export function LandingPage() {
  return (
    <Container>
      <Stack spacing={2} sx={{ py: 6 }}>
        <Typography variant="h3">MarketScout AI</Typography>
        <Typography>Educational stock and ETF discovery with transparent AI-assisted screening.</Typography>
        <Typography variant="h6">Example workflows</Typography>
        <Typography>• Dividend-paying technology stocks similar to Microsoft with lower valuation.</Typography>
        <Button component={Link} to="/discover" variant="contained">Open Discovery Dashboard</Button>
      </Stack>
    </Container>
  );
}

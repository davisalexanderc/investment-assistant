import { Container, Grid, Stack, Typography } from '@mui/material';
import { AgentTracePanel } from '../components/AgentTracePanel';
import { AIAssistantPanel } from '../components/AIAssistantPanel';
import { FilterPanel } from '../components/FilterPanel';
import { ResultsTable } from '../components/ResultsTable';

export function DiscoveryPage() {
  return (
    <Container maxWidth="xl" sx={{ py: 3 }}>
      <Stack spacing={2}>
        <Typography variant="h4">Discovery Dashboard</Typography>
        <Grid container spacing={2}>
          <Grid item xs={12} md={3}><FilterPanel /></Grid>
          <Grid item xs={12} md={6}><ResultsTable /></Grid>
          <Grid item xs={12} md={3}>
            <Stack spacing={2}>
              <AIAssistantPanel />
              <AgentTracePanel />
            </Stack>
          </Grid>
        </Grid>
      </Stack>
    </Container>
  );
}

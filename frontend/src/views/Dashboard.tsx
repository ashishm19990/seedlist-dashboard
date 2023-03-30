import React, { useEffect } from 'react';
import { Typography, Container, Box } from '@mui/material';
import Paper from '@mui/material/Paper';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import { Switch, Button } from '@mui/material';
import { useLazyQuery } from '@apollo/client';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import Select from '@mui/material/Select';
import { SEED_ISPS } from '../gql/Queries';
import { getNullableType, GraphQLNonNull } from 'graphql';

const columns: GridColDef[] = [
  {
    field: 'name',
    headerName: 'Name',
    width: 500,
  },
  {
    field: 'toggle',
    headerName: 'On/Off',
    sortable: false,
    width: 200,

    renderCell: (params) => {
      return (
        <div className="d-flex justify-content-between align-items-center" style={{ cursor: 'pointer' }}>
          <Switch value={params.row.id} defaultChecked />
        </div>
      );
    },
  },

  {
    field: 'actions',
    headerName: 'Actions',
    sortable: false,
    width: 300,
    renderCell: (params) => {
      return (
        <div className="d-flex justify-content-between align-items-center" style={{ cursor: 'pointer' }}>
          <Button data-id={params.row.id} variant="contained">
            View Seeds
          </Button>{' '}
          <Button data-id={params.row.id} variant="contained" color="error">
            Delete
          </Button>
        </div>
      );
    },
  },
];

export default function Dashboard() {
  const [isps, setIsps] = React.useState([]);
  const [ispId,setIspId] = React.useState(0);

  const [fetchIsps] = useLazyQuery(SEED_ISPS, {
    onCompleted: (data) => {
      setIsps(data.isps);
    },
    onError: (data) => {
      console.log(data);
    },
  });

  useEffect(() => {
    const onPageLoad = () => {
      fetchIsps();
    };
    onPageLoad();
  }, []);

  function handleIspChange(event){
    setIspId(event.target.value)
}

  return (
    <Box
      component="main"
      sx={{
        backgroundColor: (theme) =>
          theme.palette.mode === 'light' ? theme.palette.grey[100] : theme.palette.grey[900],
        pt: 4,
        pb: 4,
      }}
    >
      <Container maxWidth="lg">
        <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
          <Typography component="h2" variant="h6" color="primary" gutterBottom>
            Seedlist Dashboard
          </Typography>
          <div>
            <FormControl sx={{ my: 1, minWidth: 150 }} size="small">
              <InputLabel id="isp_id">ISP Selection</InputLabel>
              <Select labelId="isp_id" id="isp_id" displayEmpty label="ISP Selection" onChange={handleIspChange}>
                <MenuItem value='0'>
                  <em>All</em>
                </MenuItem>
                {isps &&
                  isps.map((item, index) => (
                    <MenuItem key={index} value={item.id}>
                      {item.name}
                    </MenuItem>
                  ))}
              </Select>
            </FormControl>
          </div>
          <div style={{ height: 400, width: '100%' }}>
            <DataGrid rows={isps.filter(function(isp) {
                            return (ispId == 0) || (isp.id == ispId);
                            })} 
              columns={columns} pageSize={5} rowsPerPageOptions={[5]} />
          </div>
        </Paper>
      </Container>
    </Box>
  );
}

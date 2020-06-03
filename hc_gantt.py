import dash
import dash_alternative_viz as dav

today = 1580860800000
day = 86400000
gantt = {
 'title': {
   'text': 'Intraday jobs Scheduling'
 },
 'xAxis': {
   'currentDateIndicator': True,
   'min': today + 0.75 * day,
   'max': today + 1.1 * day,
 },
 'series': [{
   'name': 'Init M1, Import FIRT market data',
   'data': [{
     'taskName': 'Init M1, Import FIRT market data',
     'id': 'FIRT',
     'start': today + 1000 * (18 * 3600 + 13 * 60 + 30),
     'end': today + 1000 * (23 * 3600 + 59 * 60 + 24)
   }, {
     'taskName': '<b>FI1MRA1A</b>: CleanupSAS.ksh',
     'id': 'FI1MRA1A',
     'parent': 'FIRT',
     'start': today + 1000 * (19 * 3600 + 13 * 60 + 30),
     'end': today + 1000 * (19 * 3600 + 30 * 60 + 24)
   }, {
     'taskName': '<b>FI1MRA1B</b>: INIT_MRE.ksh',
     'id': 'FI1MRA1B',
     'parent': 'FIRT',
     'start': today + 1000 * (20 * 3600 + 13 * 60 + 30),
     'end': today + 1000 * (20 * 3600 + 30 * 60 + 24),
     'dependency': 'FI1MRA1A'
   }, {
     'taskName': '<b>FI1MRA1C</b>: MKD_files_transfert.ksh',
     'id': 'FI1MRA1C',
     'parent': 'FIRT',
     'start': today + 1000 * (21 * 3600 + 13 * 60 + 30),
     'end': today + 1000 * (22 * 3600 + 30 * 60 + 24),
     'dependency': 'FI1MRA1B'
   }, {
     'taskName': '<b>FI1MRA1D</b>: Corporate_Events.ksh',
     'id': 'FI1MRA1D',
     'parent': 'FIRT',
     'start': today + 1000 * (22 * 3600 + 13 * 60 + 30),
     'end': today + 1000 * (22 * 3600 + 30 * 60 + 24)
   }, {
     'taskName': '<b>FI1MRA1G</b>: extract_mrcatetb.ksh',
     'id': 'FI1MRA1G',
     'parent': 'FIRT',
     'start': today + 1000 * (23 * 3600 + 13 * 60 + 30),
     'end': today + 1000 * (23 * 3600 + 30 * 60 + 24)
   }, {
     'taskName': '<b>FI1MRA2B</b>: DLY_BATCH.F1.SETUP_RUNDATE.ksh',
     'id': 'FI1MRA2B',
     'parent': 'FIRT',
     'start': today + 1000 * (23 * 3600 + 13 * 60 + 30),
     'end': today + 1000 * (23 * 3600 + 50 * 60 + 24)
   }, {
     'taskName': '<b>FI1MRL1A</b>: FillDMMPBKTB2.ksh',
     'id': 'FI1MRL1A',
     'parent': 'FIRT',
     'start': today + 1000 * (23 * 3600 + 50 * 60 + 30),
     'end': today + 1000 * (23 * 3600 + 55 * 60 + 24),
     'dependency': 'FI1MRA2B'
   }]
 }]
}

nongantt = {
          'title': {
            'text': 'My chart'
          },
          'series': [{
            'data': [1, 2, 3]
          }]
        }

app = dash.Dash(__name__)
app.layout = dav.HighChart(
        options=gantt,
        constructorType='ganttChart'
)



if __name__ == '__main__':
    app.run_server(debug=True)

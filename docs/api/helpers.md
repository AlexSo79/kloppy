# Helpers

## Loading event data

All event load functions support [options](#options).

::: kloppy.load_datafactory_event_data

::: kloppy.load_statsbomb_event_data
      
::: kloppy.load_opta_event_data

::: kloppy.load_metrica_json_event_data

::: kloppy.load_sportec_event_data

::: kloppy.load_wyscout_event_data


### Options

Option | Type | Description | Default
------ | ---- | ----------- | -------
**`event_types`** | `List[str]` | Only load events of these types to the dataset. By default load all types. See [`EventTypes`][kloppy.domain.models.event.EventType]. Pass the name of the EventType. Example `["PASS", "SHOT"]` | None

## Loading tracking data

::: kloppy.load_tracab_tracking_data

::: kloppy.load_skillcorner_tracking_data

::: kloppy.load_metrica_csv_tracking_data

::: kloppy.load_metrica_epts_tracking_data

::: kloppy.load_second_spectrum_tracking_data

## Other helpers

::: kloppy.domain.services.state_builder.add_state

::: kloppy.helpers.to_pandas

::: kloppy.helpers.transform
    
 
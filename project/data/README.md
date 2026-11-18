# ActivityPulse anonymized sample dataset

Derived from two activity-tracking worksheets, retaining a row-level activity pattern while removing names, employer identities, titles, URLs, notes, exact dates, source IDs, and financial amounts. Dates are relative offsets, organizations are generic labels, and participants are user_1 and user_2. Values are anonymized demonstration data, not suitable for reconstructing original records. No private crosswalk is committed. Dataset contains 117 records.

Use `activitypulse-activities.csv` for the CLI baseline. The original source worksheets remain untouched.

## Interpretation limits

The CSV was already committed before this reconciliation. All 117 rows are preserved unchanged. The source documentation does not provide a reproducible export procedure or private crosswalk, so this review verifies the saved structure and row count, not a complete record-by-record reconstruction of the private trackers.

Despite its name, `duration_hours` can contain fixed reporting credits (for example, an application credit) as well as supported manual durations. It is not a uniform measure of elapsed work. A blank value means no recorded amount; zero is a distinct recorded value and must not be converted to missing. Relative day labels preserve offsets; file order is not necessarily chronological. Generic participant/organization labels and retained patterns are for demonstration and do not guarantee resistance to reidentification if combined with outside information.

Do not use this demonstration file to backfill actual project time, infer PATH eligibility, or restore private names. Original records and any duration clarification belong in their private trackers. These data files are informational artifacts; no loader or application has been implemented.


'use strict';

const { spawnSync } = require('node:child_process');
const path = require('node:path');

console.log('Hello World!');
console.log('I am ActivityPulse v0.1');

const reporter = path.join(__dirname, 'report.py');

const result = spawnSync('python3.12', [reporter], {
  encoding: 'utf8'
});

if (result.error) {
  console.error('Could not launch Python:', result.error.message);
  process.exit(1);
}

if (result.status !== 0) {
  console.error('Python reporter failed:', result.stderr);
  process.exit(result.status ?? 1);
}

const summary = JSON.parse(result.stdout);

console.log('\nActivity Summary');
console.log(`Total records: ${summary.total_records}`);

for (const [type, count] of Object.entries(summary.by_activity_type)) {
  console.log(`${type}: ${count}`);
}

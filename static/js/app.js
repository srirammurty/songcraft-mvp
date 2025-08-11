async function callApi(path, body){
  const resp = await fetch(path, {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify(body)
  });
  return resp.json();
}

async function generateInstrumental(){
  const prompt = document.getElementById('prompt').value;
  const duration = parseInt(document.getElementById('duration').value || "20");
  document.getElementById('instStatus').innerText = 'Queued...';
  const data = await callApi('/api/generate/instrumental', {prompt, duration});
  const jobId = data.job_id;
  addJob(jobId);
}

async function generateVocals(){
  const text = document.getElementById('lyrics').value;
  document.getElementById('vocStatus').innerText = 'Queued...';
  const data = await callApi('/api/generate/vocals', {text});
  addJob(data.job_id);
}

function addJob(jobId){
  const jobsDiv = document.getElementById('jobs');
  const el = document.createElement('div');
  el.id = "job_" + jobId;
  el.innerHTML = `<strong>${jobId}</strong> - <span class="status">running</span> - <a href="#" onclick="downloadJob('${jobId}'); return false;">Download</a>`;
  jobsDiv.prepend(el);
  pollJob(jobId);
}

async function pollJob(jobId){
  const el = document.getElementById('job_' + jobId);
  const statusSpan = el.querySelector('.status');
  const res = await fetch('/api/job/' + jobId);
  const data = await res.json();
  statusSpan.innerText = data.status || 'unknown';
  if(data.status === 'done'){
    el.querySelector('a').href = '/download/' + jobId;
  } else if (data.status === 'running'){
    setTimeout(()=>pollJob(jobId), 2000);
  } else {
    // show error
    el.innerText += " (error)";
  }
}

function downloadJob(jobId){
  window.location = '/download/' + jobId;
}

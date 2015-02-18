/*
 * Copyright 2015 NEC Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.o3project.odenos.core.component.network.flow.query;

import org.o3project.odenos.core.component.network.BaseObjectQuery;
import org.o3project.odenos.core.component.network.flow.Flow;
import org.o3project.odenos.core.component.network.topology.Topology;

/**
 * Prepares a query for Flow class.
 *
 */
public abstract class FlowQuery extends BaseObjectQuery<Flow> {

  protected Topology topology = null;

  /**
   * Constructor.
   * @param queriesString query string.
   */
  public FlowQuery(String queriesString) {
    super(queriesString);
  }

  /**
   * Sets a topology.
   * @param topology topology.
   */
  public void setTopology(Topology topology) {
    this.topology = topology;
  }
}